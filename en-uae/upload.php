<?php
session_start();
include('connection.php');
$conn->query('delete from test');
if($_SERVER['REQUEST_METHOD'] == "POST")
{
	$file = addslashes($_FILES["csv-file"]["tmp_name"]);
	$query = <<<eof
LOAD DATA INFILE '$file'
INTO TABLE test
FIELDS TERMINATED BY ';' 
eof;
	print_r( $sql);
	// $res=$conn->query("select * from wadi_uae_cat");
	// $result=array();
	// while ($result[]=mysqli_fetch_assoc($res)){}
	// $handle = fopen($_FILES['csv-file']['tmp_name'], "r");
	// while (($data = fgetcsv($handle, 0, ";")) !== FALSE){

	// 	$id=0;
	// 	$sql="insert into test(Device_ID,Name,Category,Image,Model,Brand,Color,Url,New_Price,Old_Price) values("."'".$data[0]."'".","."'".$data[1]."'".","."'".$data[2]."'".","."'".$data[3]."'".","."'".$data[4]."'".","."'".$data[5]."'".","."'".$data[6]."'".","."'".$data[7]."'".","."'".$data[8]."'".","."'".$data[9]."'".")";
	// 	// echo ('<br>'.$sql);
	// 	// for ($i=0;$i<count($result);$i++){
	// 	// 	if(strtolower($result[$i]['Category'])==strtolower($data[2])){
	// 	// 		$id=$result[$i]['id'];
	// 	// 		break;
	// 	// 	}
	// 	// }
	// 	// if($id==0){
	// 	// 	echo '<br>'."Category for product - ".$data[0]." not found in database".'<br>';
	// 	// 	continue;
	// 	// }
	// 	// $sql="insert ignore into test(Device_ID,Name,Category,Image,Model,Brand,Color,Url,New_Price,Old_Price) values("."'".$data[0]."'".","."'".$data[1]."'".",".$id.","."'".$data[3]."'".","."'".$data[4]."'".","."'".$data[5]."'".","."'".$data[6]."'".","."'".$data[7]."'".","."'".$data[8]."'".","."'".$data[9]."'".")";
	// 	// // print($sql);
		if(!$conn->query($sql))
			echo mysqli_error($conn);
	// }
	//header('Location:index.php');
}

?>