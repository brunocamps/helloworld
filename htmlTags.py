
htmlText = """
<!DOCTYPE html>
<html>
	<head>
		<title>Chapter 5, the 9 Essential tags</title>
	</head>
	<body>

	<h1>Stef's 9 Essential HTML Tags:</h1>

	<h1>h, p , a, br, img, ul, ol, li, div</h1>

	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. <br>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.<br> Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum</p>


	</body>
</html>"""

htmlTags = ["<div>", "</div>", "<br>", "</br>", "<ol>", "</ol>", "<head>", "</head>"]

if "<h1>" in htmlText:
    print("True for h1")


if htmlTags[0] or htmlTags[1] in html:
    print("true")

#Encontrar se o texto em HTML contem a tag div a partir da array htmlTags

if htmlTags[0] and htmlTags[1] in htmlText:
    print("True for <div>")
else:
    print("The HTML doesn't contain <div>")


 #checar se possui a tag <head> (htmlTags[6], htmlTags[7])
if htmlTags[6] and htmlTags[7] in htmlText:
    print("True for <head>")
else:
    print("The HTML doesn't contain <head>")


#Arquivo para encontrar tokens do html

