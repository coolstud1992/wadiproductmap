<?php
$servername = "localhost";
$username = "root";
$password = "";

// Create connection
$conn = mysqli_connect($servername, $username, $password, 'wadi');

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}