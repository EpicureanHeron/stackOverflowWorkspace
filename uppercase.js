function titleCase(str) {
  let strArray = str.split('');
  strArray[0].toUpperCase();
  for(let i=0;i<strArray.length;i++){
    if(strArray[i]!==' '){
      strArray[i] = strArray[i].toUpperCase();
    }
  }
  return strArray.join('');
}

let titleStr = titleCase("i'm a little tea pot");
console.log(titleStr);