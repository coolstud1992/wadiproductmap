<?php
session_start();
	include('connection.php');
	$souq=$_POST['souq'];
	$items=$_POST['items'];
	//print_r($souq);
	for($i=0;$i<count($items);$i++)
	{
		//echo $souq[(int)$items[$i]]['name'];
		$sql="insert into mappings (Device_ID,souq_name,souq_url,souq_price_old,souq_price_new,souq_img,mapped_by)".
		" values("."'".$_POST["item"]["Device_ID"]."'".","."'".$souq[(int)$items[$i]]["name"]."'".
		","."'".$souq[(int)$items[$i]]["url"]."'".","."'".$souq[(int)$items[$i]]["oldprice"]."'".","."'".$souq[(int)$items[$i]]["newprice"]."'".","."'".$souq[(int)$items[$i]]["img"]."'".
		",".$_SESSION['user'].")";
		print_r($_SESSION);
		if(!$conn->query($sql))
			echo mysqli_error($conn);
	
	}
	$conn->close();
?>