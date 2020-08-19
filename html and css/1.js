<html>
<body>
<img id='img' width="500" height="600">
<script>
var str = "<p>Hello</p><p style=\"text-align: center; \"><img src=\"https://i.stack.imgur.com/CE5lz.png\" alt=\"\"><br></p><p style=\"text-align: center; \">Hello</p><br><p style=\"text-align: center; \"><img src=\"https://www.google.co.th/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png\" alt=\"\"><br></p><p style=\"text-align: left;\">Hello World</p><br><br><br>";
var elem = document.createElement('div');
elem.style.display = 'none';
document.body.appendChild(elem);
elem.innerHTML = str;
console.log(elem.querySelector('img').src);
document.getElementById("img").src = "https://i.stack.imgur.com/CE5lz.png";
</script>

</body>
</html>