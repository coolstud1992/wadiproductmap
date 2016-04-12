<?php
session_start();
include('connection.php');
$id=$_POST['item'];
$sql="select * from wadi_uae where ID=$id";
if(!$res=$conn->query($sql))
	echo mysqli_error($conn);
else{
	$result=mysqli_fetch_assoc($res);
	//$result=json_encode($result);
	//checking if dvice is already mapped or not
	$sql="select Device_ID from mappings where Device_ID="."'".$result['Device_ID']."'";
	if(!$res=$conn->query($sql))
		echo mysqli_error($conn);
	else
		{
			$result2=mysqli_fetch_assoc($res);
			if(count($result2)==1)
				print_r("found");
			else
				echo(json_encode($result));
		}	
	
	 }
$conn->close();
