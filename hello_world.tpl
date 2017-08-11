<!DOCTYPE html>

<html>
<head>
    <title>hello mongo</title>
</head>
<body>

<ul>
    %for i in names:
    <li>{{i['name']}}</li>
    %
</ul>

<form action="/fav_person" method="POST">
    who is your favourite
    <input type="text" name="person" size="40"><br>
    <input type="submit" value="Submit">
</form>

</body>
</html>