<?php
include 'config.php'; // FLAG is defined in config.php

if (preg_match('/config\.php\/*$/i', $_SERVER['PHP_SELF'])) {
	  exit("I don't know what you are thinking, but I won't let you read it :)");
}

if (isset($_GET['source'])) {
	  highlight_file(basename($_SERVER['PHP_SELF']));
	    exit();
}

$secret = bin2hex(random_bytes(64));
if (isset($_POST['guess'])) {
	  $guess = (string) $_POST['guess'];
	    if (hash_equals($secret, $guess)) {
		        $message = 'Congratulations! The flag is: ' . FLAG;
			  } else {
				      $message = 'Wrong.';
				        }
}
?>
<!doctype html>
<html lang="en">
  <head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>Cyber Security Challenge</title>
    <meta charset="UTF-8">
    <meta name="keywords" content="Cyber, Security, Challenge, Waikato, Competition, University, Server, Crow, Encryption, SQL, Injection, Drone, IT, Server, Side, Protection, Attack, Defend">
    <meta name="description" content="The NZ Cyber Security Challenge is back! A huge competition involved around the idea of security on the internet. Jump in and register for your share of workshops, challenges, prizes and presentations.">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/ico" href="files/assets/favicon.ico">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" media="screen and (min-width: 950px)" href="files/css/web.css">
    <link rel="stylesheet" media="screen and (max-width: 950px)" href="files/css/phone.css">
    <link href="files/css/font.css" rel="stylesheet">
    <script src="files/scripts/javaScript.js"></script>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.11.1.js"></script>      
  </head>
  <body>
    <div class="navbar">
      <div class="navbar__logo">
        <span class="navbar__logo__home">
            <i class="fa fa-home" onclick="window.open('/home/','_blank')"></i>
        </span>
        <img class="navbar__logo__image" src="files/assets/csc_watermark.png" alt="NZCSC-logo">
      </div>
      <div class="navbar__content">
        <div class="mobile">
               <select id="SELECT" onchange="selection();">
                  <option value="0" selected="selected">HOME</option>
                  <option value="1">CH1</option>
                  <option value="2">CH2</option>
                  <option value="3">CH3</option>
                  <option value="4">CH4</option>
                  <option value="5">CH5</option>
                  <option value="6">CH6</option>
                  <option value="7">CH7</option>
                  <option value="8">CH8</option>
                  <option value="9">CH9</option>
                  <option value="10">CH10</option>
                  <option value="11">CH11</option>
                  <option value="12">CH12</option>
                  <option value="13">CH13</option>
                  <option value="14">CH14</option>
               </select>
            </div>
            <div class="navbar-buttons">
               <div class="navbar__button__container">
                  <button type="button" onclick="window.open('/challenge1/','_blank')" class="navbar__button" id="CH1-BUTTON">Challenge 1</button>
                  <button type="button" onclick="window.open('/challenge2/','_blank')" class="navbar__button" id="CH2-BUTTON">Challenge 2</button>               
                  <button type="button" onclick="window.open('/challenge3/','_blank')" class="navbar__button" id="CH3-BUTTON">Challenge 3</button>
                  <button type="button" onclick="window.open('/challenge4/','_blank')" class="navbar__button" id="CH4-BUTTON">Challenge 4</button>
                  <button type="button" onclick="window.open('/challenge5/','_blank')" class="navbar__button" id="CH5-BUTTON">Challenge 5</button>
               </div>
               <div class="navbar__button__container"> 
                  <button type="button" onclick="window.open('/challenge6/','_blank')" class="navbar__button" id="CH6-BUTTON">Challenge 6</button>
                  <button type="button" onclick="window.open('/challenge7/','_blank')" class="navbar__button" id="CH7-BUTTON">Challenge 7</button>
                  <button type="button" onclick="window.open('/challenge8/','_blank')" class="navbar__button" id="CH8-BUTTON">Challenge 8</button>
                  <button type="button" onclick="window.open('/challenge9/','_blank')" class="navbar__button" id="CH9-BUTTON">Challenge 9</button>
                  <button type="button" onclick="window.open('/challenge10/','_blank')" class="navbar__button" id="CH10-BUTTON">Challenge 10</button>
               </div>
               <div class="navbar__button__container">
                  <button type="button" onclick="window.open('/challenge11/','_blank')" class="navbar__button" id="CH11-BUTTON">Challenge 11</button>
                  <button type="button" onclick="window.open('/challenge12/','_blank')" class="navbar__button" id="CH12-BUTTON">Challenge 12</button>
                  <button type="button" onclick="window.open('/challenge13/','_blank')" class="navbar__button" id="CH13-BUTTON">Challenge 13</button>
                  <button type="button" onclick="window.open('/challenge14/','_blank')" class="navbar__button" id="CH14-BUTTON">Challenge 14</button>
              <button type="button" onclick="window.open('/challenge15/','_blank')" class="navbar__button" id="CH15-BUTTON">Challenge 15</button>
        </div>
            </div>
      </div>
    </div>
    <div class="page__content">
      <div class="page__content__logo">
        <img src="files/assets/crow_gold.png" alt="themelogo">
      </div>
      <div class="page__content__container">
        <div class="page__content__data">
          <h4 style="color:#1E90FF;">There are two ways you can get this flag. One is by guessing the hex number and the other is through the source.</h4>
          <p><a href="?source">Source</a></p>
          <hr>
          <?php if (isset($message)) { ?>
              <p><?= $message ?></p>
          <?php } ?>
          <form action="/challenge7/" method="POST">
            <input type="text" name="guess">
            <input type="submit">
          </form>
        </div>
      </div>
    </div>
  </body>
</html>
