param([switch]$VerifyOnly, [string]$ProjectName, [string]$Destination)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem
function Get-ArchiveSha256([string]$Path) {
    $stream = [IO.File]::OpenRead($Path)
    $hasher = [Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($hasher.ComputeHash($stream)).Replace('-', '').ToLowerInvariant() }
    finally { $hasher.Dispose(); $stream.Dispose() }
}
$bundleRoot = $PSScriptRoot
if (-not $Destination) { $Destination = Join-Path $bundleRoot 'PROJECTS' }
$destinationFull = [IO.Path]::GetFullPath($Destination)
$manifest = Get-Content -LiteralPath (Join-Path $bundleRoot 'MANIFEST.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$projects = @($manifest.projects)
if ($ProjectName) {
    $projects = @($projects | Where-Object { $_.project -ceq $ProjectName })
    if ($projects.Count -ne 1) { throw 'Unknown project name.' }
}
foreach ($project in $projects) {
    $archive = Join-Path $bundleRoot $project.backup
    if ((Get-ArchiveSha256 $archive) -ne $project.backup_sha256) {
        throw "Backup checksum mismatch: $($project.project)"
    }
    $target = Join-Path $destinationFull $project.project
    if ((Test-Path -LiteralPath $target) -and -not $VerifyOnly) { throw "Target already exists; choose a new empty destination: $target" }
    $zip = [IO.Compression.ZipFile]::OpenRead($archive)
    try {
        $seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
        foreach ($entry in $zip.Entries) {
            $relative = $entry.FullName.Replace('\', '/')
            if (-not $relative.StartsWith($project.project + '/', [StringComparison]::Ordinal)) { throw 'Unexpected archive root.' }
            if ($relative.Contains(':') -or ($relative.Split('/') -contains '..')) { throw 'Unsafe archive path.' }
            $resolved = [IO.Path]::GetFullPath((Join-Path $destinationFull $relative))
            if (-not $resolved.StartsWith($destinationFull.TrimEnd('\') + '\', [StringComparison]::OrdinalIgnoreCase)) { throw 'Archive escapes destination.' }
            if (-not $seen.Add($resolved)) { throw 'Duplicate archive path.' }
        }
        if (-not $seen.Contains((Join-Path $target 'tobii.project'))) { throw 'Missing tobii.project.' }
    } finally { $zip.Dispose() }
    Write-Host "Verified: $($project.project)"
}
if ($VerifyOnly) { Write-Host "PASS: $($projects.Count) native backups verified."; exit 0 }
[IO.Directory]::CreateDirectory($destinationFull) | Out-Null
foreach ($project in $projects) {
    [IO.Compression.ZipFile]::ExtractToDirectory((Join-Path $bundleRoot $project.backup), $destinationFull)
    Write-Host "Restored: $($project.project)"
}
Write-Host "DONE: $($projects.Count) projects restored to $destinationFull"
Write-Host 'Open the selected PROJECTS/<project>/tobii.project in Tobii Pro Lab. Hardware acceptance is still pending.'
