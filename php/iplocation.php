<?php

//Your justreqit.com access_token
$access_token = 'changeme';

function ip_location($ip) {
	global $access_token;
	$api_url = 'https://justreqit.com/api/ipv4/'.$ip.'/?access_token='.$access_token;
	$response = json_decode(file_get_contents($api_url));
	if ($response->status == "success"){
		return $response->results->city.', '.$response->results->state;
	} else {
		return null;
	}
}


echo ip_location("140.82.112.3");


?>