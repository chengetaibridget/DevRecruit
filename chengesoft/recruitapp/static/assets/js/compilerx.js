let editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/c_cpp");
}

function changeLanguage() {

    let language = $("#languages").val();

    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'php')editor.session.setMode("ace/mode/php");
    else if(language == 'python')editor.session.setMode("ace/mode/python");
    else if(language == 'node')editor.session.setMode("ace/mode/javascript");
}

function executeCode() {
    var xhr = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/compiler";
    
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    
    var language = document.getElementById("languages").value;
    var code = editor.getSession().getValue();
    var data = "language=" + encodeURIComponent(language) + "&code=" + encodeURIComponent(code);
    
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = xhr.responseText;
        document.querySelector(".output").textContent = response;
      }
    };
    
    xhr.send(data);
  }

