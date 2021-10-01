<?php
function curl_command(){
    $url = '';
    if (isset($_POST['vlannumber'])&&isset($_POST['vlanname'])&&isset($_POST['vlanip'])&&isset($_POST['vlanmask'])){
        $url = "http://127.0.0.2:5000/{$_POST['vlannumber']}/{$_POST['vlanname']}/{$_POST['vlanip']}/{$_POST['vlanmask']}";
    }

    if (filter_var($url, FILTER_VALIDATE_URL) === FALSE) {//Checking if the url is valid if its not then it means its probably just an ampty string
        echo 'No valid inputs?!?';
    }else{//Curl configs setup
        $curl = curl_init();
        curl_setopt($curl, CURLOPT_URL,$url);
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER,false);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
        
        $result = curl_exec($curl);
        echo $result;
        curl_close($curl);
    }
}
