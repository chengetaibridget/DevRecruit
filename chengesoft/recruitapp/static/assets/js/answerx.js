function saveAnswer() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  
    var code = editor.getSession().getValue();
    var params = "code=" + encodeURIComponent(code);
  
    xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        location.replace('/recruit');
      }
    };
  
    xhr.send(params);
  }