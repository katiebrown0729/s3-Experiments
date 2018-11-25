<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>All Data</title>
<!--<link href="piled.css" rel="stylesheet" type="text/css">-->
<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/piled.css') }}">
</head>

<body>
    <h1> All Data </h1>
    <main-content class="main">
        <p>
           Total number of readings is: {{data.__len__()}}
            <table border="1" width="100%">
                <tr>
                    <th>Serial Number</th>
                    <th>Timestamp</th>
                    <th>X</th>
                    <th>Y</th>
                    <th>Z</th>
                </tr>
            {% for reading in data %}
                <tr>
                    <td>{{reading['serial-no']}}</td>
                    <td>{{reading['timestamp']}}</td>
                    <td>{{reading['x']}}</td>
                    <td>{{reading['y']}}</td>
                    <td>{{reading['z']}}</td>
                </tr>
            {% endfor %}
            </table>
        </p>
</main-content>

<br>
<br>
All Data
</body>
</html>