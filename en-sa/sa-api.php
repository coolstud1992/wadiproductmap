<?php

	if($_SERVER['REQUEST_METHOD']=="GET"){
		include('connection.php');
		$response['success']='false';
		$response['data']=0;
		$keys=array_keys($_GET);
		foreach($keys as $k){
			if($k=='fetch'){  //to fetch wadi product
				$sql="Select * from wadi_sa where ID=$_GET[$k]";
				$res=$conn->query($sql);
				$result=mysqli_fetch_assoc($res);
				$response['data']=$result;
				$response['success']="true";

			}

			if($k=='fetchsouq'){		//to fetch souq product
				$sql="select * from look where Device_ID='$_GET[$k]'";
				$res=$conn->query($sql);
				$result=array();
				while($result[]=mysqli_fetch_assoc($res)){}
				$response['data']=$result;
				$response['success']="true";

			}

			if ($k=='checkmap'){
				$sql="select * from mappings_sa where Device_ID='$_GET[$k]'";
				$res=$conn->query($sql);
				$result=array();
				while($result[]=mysqli_fetch_assoc($res)){}
				$response['data']=$result;
				$response['success']="true";
				
			}

			if($k=='map'){
			
			}
		}
		echo json_encode($response);
	}

	?>