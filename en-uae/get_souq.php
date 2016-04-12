<?php
session_start();
$wadi=$_POST['wadi'];
$sql="select * from look where Device_ID='$wadi'";
include('connection.php');
$res=$conn->query($sql);
if($res){
	$result=array();
	while($result[]=mysqli_fetch_assoc($res)){}
	print(json_encode($result));
}
else
	echo "error encountered";
?>