
<!-- https://localhost/dashboard/index.php?day=28&month=9&year=2021 -->
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="includes/stylesheet.css">
    <meta charset="UTF-8">
    <script
    src="https://code.jquery.com/jquery-3.4.1.min.js"
    integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo="
    crossorigin="anonymous"></script>
</head>
<body>
   
<div class="terminalbox-wrapper">
    <div id="scrollerbox" class="terminalbox"> 
        <div style='max-width: 375px;' id="file_content"></div>   
    </div>
    <div id="scrollerbox" class="terminalbox">  
        <?php require_once 'commandsender.php';
               curl_command(); ?> 
    </div>
   <form name="addres" id="addres" method="post" action="" class="vlanform">
    <div >
    <span>Vlan number:<input type="text" name="vlannumber"><br></span>
        <span>Vlan name:<input type="text" name="vlanname"><br></span>
        <span>vlan ip:<input type="text" name="vlanip"><br></span>
        <span>vlan mask:<input type="text" name="vlanmask"><br></span>
       <input type="submit" class="btn"/>
    </div>
</form>
</div>
<form name="addres" id="addres" method="get" action="">
    <div style='display:flex; justify-content:center;'>
        <span>Day:<input type="text" name="day"><br></span>
        <span>month:<input type="text" name="month"><br></span>
        <span>year:<input type="text" name="year"><br></span>
       <input type="submit" class="btn"/>
    </div>
</form>


<script type="text/javascript" src ='includes/ajax.js'>terminal_loader();//Ajax will keep loading the logfile so if there is any changes it will be updated "live"</script> 
<script type="text/javascript"> terminal_loader();</script>

</body>