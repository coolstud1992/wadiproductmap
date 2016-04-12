<?php
session_start();
include('connection.php');
$sql="select * from mappings where Device_ID="."'".$_POST['item']['Device_ID']."'";
//echo $sql;
if(!$result=$conn->query($sql))
{
	echo "error";
}
else
{
$res=array();
while($res[]=mysqli_fetch_assoc($result)){
}
$res=json_encode($res);
echo $res;
}
$conn->close();
?>