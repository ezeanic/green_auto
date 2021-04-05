<!DOCTYPE html>
<html>
<head>
  <title>Driving Information Results</title>
</head>
<body>
  <h1>Information</h1>
  <?php
    
   
    $host = "database-1.cnce4t16eacl.us-east-1.rds.amazonaws.com";
    $user = "ciszara";
    $pass = "password";
    $db = "green_auto";
    $port = "3306";
   
    //$searchtype=$_POST['searchtype'];
    $searchterm=$_POST['searchterm'];

    

    $conn = mysqli_connect($host, $user, $pass, $db, $port);
    $statement = "SELECT * FROM drive WHERE time=$searchterm;";
    $result = $conn->query($statement);
    $num_results = $result->num_rows;
    
    if ($num_results == 0) {
       echo '<p>You have not entered search details.<br/>
       Please go back and try again.</p>';
       exit;
    }
    
    while($row = $result->fetch_assoc()){
         echo "<h4> Timestamp: {$row["time"]} </h4>";
         echo "<p>Speed: {$row["speed"]}</p>";
         echo "<p>RPM: {$row["RPM"]}</p>";
         echo "<p>Throttle: {$row["throttle"]}</p>";
         echo "<p>Coolant Temperature: {$row["coolant_temp"]}</p>";
         echo "<p>Intake Temperature: {$row["intake_temp"]}</p>";
     }
     
    
    $db->close();
  ?>

  
</body>
</html>

