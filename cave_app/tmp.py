{% load staticfiles %}
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
<!doctype html>
<html>
<head>
  <title>Guam Groundwater Research Project</title>
  <link rel="stylesheet" href="{%static 'css/style.css' %}" />
</head>
<body>
  <button type="button">Enter Data</button>
  <button type="button">Download Data</button>
  <h1><a href="">Things are happening</a></h1>
  <p>Once I've figure out how to do this</p>
  <select name="Location">
  {% for loc in loc %}
    <option value="{{loc.Location}}">{{loc.location}}</option>
  {% endfor %}
  </select>
</body>
</html>
