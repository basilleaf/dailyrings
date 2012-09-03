<?php

// shit on a shingle, this is php!!!

// posts to fb, runs on cron

include('secrets.php');
require_once '~/facebook/client/facebook.php';
include('~/facebook/fb_ini.php');

// get today's data from planetaryrings.org
if ($fp = fopen('http://www.planetaryrings.org/?fmt=json', 'r')) {
   $content = '';
   // keep reading until there's nothing left 
   while ($line = fread($fp, 1024)) {
      $content .= $line;
	}
}else {
    echo "could not open stream to http://www.planetaryrings.org/?fmt=json";
    die;
}

$content = json_decode($content);

$name = $content->{'name'};
$title = $content->{'title'};
$caption = $content->{'caption'};
$jpg = $content->{'jpg'};
$str_date = $content->{'str_date'};

$facebook->api_client->session_key = $session_key;
$facebook->api_client->expires = 0; 
$facebook->set_user($user_id,$session_key );

$message = ""; 

$image = array();
$image[type]="image";
$image[src]="http://media.planetaryrings.com/".$jpg;
$image[href]="http://planetaryrings.org/".$str_date;

$attachment = array();
$attachment[name] =  $title;
$attachment[href] = "http://planetaryrings.org/".$str_date;
$attachment[description] = strip_tags($caption);
$attachment[media] = array($image);

try{
    $facebook->api_client->stream_publish($message,$attachment,null,null,$page_id);
	echo "published today: \n<a href = \"".$image[href]."\">".$image[href]."\n\n $title \n $caption";
} catch(Exception $o ){
    print_r($o);
}

?>
