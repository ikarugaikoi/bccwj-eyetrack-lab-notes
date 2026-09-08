import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const root='__MASKED_LOCAL_PATH_0298__';
const source='__MASKED_LOCAL_PATH_0299__';
const output=root+'/import_compatible';
const files=(await fs.readdir(source)).filter(n=>n.endsWith('.xlsx')).sort();
await fs.mkdir(output,{recursive:true});
for(const file of files){
  const wb=await SpreadsheetFile.importXlsx(await FileBlob.load(process.argv[2]==='render'?output+'/'+file.replace('.xlsx','_TEXT8.xlsx'):source+'/'+file));
  const sh=wb.worksheets.getItem('Tobii_Design');
  if(process.argv[2]==='render'){
    const png=await wb.render({sheetName:'Tobii_Design',range:'D1:K7',format:'png',scale:1.4});
    await fs.writeFile(output+'/TEXT8_preview.png',new Uint8Array(await png.arrayBuffer()));break;
  }
  if(process.argv[2]==='inspect'){
    console.log(wb.help('workbook.render',{include:'index,examples,notes',maxChars:3500}).ndjson);
    console.log((await wb.inspect({kind:'region',sheetId:'Tobii_Design',range:'D1:K3',maxChars:1200})).ndjson);break;
  }
  const end=/order0[12]_/.test(file)?74:65;
  for(const col of ['E','G']){
    const range=sh.getRange(`${col}2:${col}${end}`);
    range.values=range.values.map(row=>[Number(row[0]).toFixed(8)]);
    range.setNumberFormat('@');
  }
  wb.recalculate();
  await (await SpreadsheetFile.exportXlsx(wb)).save(output+'/'+file.replace('.xlsx','_TEXT8.xlsx'));
  console.log(JSON.stringify({file,rows:end-1,text_columns:['DOT_H','DOT_Y']}));
}
