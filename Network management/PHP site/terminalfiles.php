<?php
if($_POST["day"] != "" && $_POST["month"] != "" && $_POST["year"] != ""){
    $file = "{$_SERVER['DOCUMENT_ROOT']}/logfiles/weblog_{$_POST["year"]}_{$_POST["month"]}_{$_POST["day"]}.txt";
}else{

    $file = "{$_SERVER['DOCUMENT_ROOT']}/logfiles/weblog_2021_9_29.txt"; //Date today this would have ben dynamic if we had a connection to the rack 24/7
}


$result = array();
clearstatcache(true, $file);
$data['time']    = filemtime($file);
$data['content'] = $_POST['time'] < $data['time']
    ? file_get_contents($file)
    : false;

echo json_encode($data);