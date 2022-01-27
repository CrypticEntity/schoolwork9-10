<?php
session_start();
// initializing variables
$firstName = "";
$email    = "";
$lastName = "";
$errors = array(); 

// connect to the database
$db = mysqli_connect('localhost', 'root', '', 'battle of bands');

// REGISTER USER
if (isset($_POST['reg_user'])) {
  // receive all input values from the form
  $firstName = mysqli_real_escape_string($db, $_POST['firstName']);
  $lastName = mysqli_real_escape_string($db, $_POST['lastName']);
  $email = mysqli_real_escape_string($db, $_POST['email']);
  $uuidquery = "UUID()";
  // form validation: ensure that the form is correctly filled ...
  // by adding (array_push()) corresponding error unto $errors array

  if (empty($firstName)) { array_push($errors, "First Name is required"); }
  if (empty($lastName)) { array_push($errors, "lastName is required"); }
  if (empty($email)) { array_push($errors, "Email is required"); }
  
  // Finally, register user if there are no errors in the form
  if (count($errors) == 0) {
  	$query = "INSERT INTO attendees (UUID, First_Name, Last_Name, email) 
  			  VALUES(uuid(), '$firstName', '$lastName', '$email')";
  	mysqli_query($db, $query);

  	$_SESSION['username'] = $firstName;
  	$_SESSION['success'] = "Registration Succsessful";
  	header('location: index.php'); 
  }
}


// LOGIN USER
if (isset($_POST['login_user'])) {
  $username = mysqli_real_escape_string($db, $_POST['username']);
  $password = mysqli_real_escape_string($db, $_POST['password']);

  if (empty($username)) {
  	array_push($errors, "Username is required");
  }
  if (empty($password)) {
  	array_push($errors, "Password is required");
  }

  if (count($errors) == 0) {
  	$query = "SELECT * FROM 'system users' WHERE username='$username' AND password='$password'";
  	$results = mysqli_query($db, $query);
  	if (mysqli_num_rows($results) == 1) {
  	  $_SESSION['username'] = $username;
  	  $_SESSION['success'] = "You are now logged in";
  	  header('location: index.php');
  	}else {
  		array_push($errors, "Wrong username/password combination");
  	}
  }
}

?>