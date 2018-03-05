<?php

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

// the facebook goo
require_once '/home/befoream/facebook/client/facebook.php';
include('/home/befoream/facebook/fb_ini.php');

$page_id ='133548456671554'; # priod page
$user_id = '1197538339';       # lballard.cat
$app_id = '20326247804'; # priod app
$session_key = 'd7d9b4e2b173d5e55429ed34-1197538339';

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
# $attachment[caption] = "My caption!";
$attachment[description] = strip_tags($caption);
$attachment[media] = array($image);

try{
    $facebook->api_client->stream_publish($message,$attachment,null,null,$page_id);
	echo "published today: \n<a href = \"".$image[href]."\">".$image[href]."\n\n $title \n $caption";
} catch(Exception $o ){
    print_r($o);
}

?>
