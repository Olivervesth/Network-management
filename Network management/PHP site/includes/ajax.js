function terminal_loader(){
    var tempdata;
    var time = 0;
    const url_string = window.location.href;
    const day = new URL(decodeURIComponent(url_string)).searchParams.get("day");
    const month = new URL(decodeURIComponent(url_string)).searchParams.get("month");
    const year = new URL(decodeURIComponent(url_string)).searchParams.get("year");
    setInterval(function() {
        $.ajax({//Ajax so we get a constant update of the file if there should be any output from the rack to the api
            type: "POST",
            data: {time : time,day : day,month : month,year : year},
            url: "terminalfiles.php",
            success: function (data) {
                var result = $.parseJSON(data)
                if (result.content && tempdata != result) {
                    $('#file_content').append('<br>' + result.content);
                    tempdata = result;
                    var objdiv = document.getElementById("scrollerbox");//migth need to fix as i dont know if the scroller will be forced down while user is holding it 
                   objdiv.scrollTo(0,document.getElementById("scrollerbox").scrollHeight);
                }
                time = result.time;
            }
        });
    }, 1000);
     
}

function command_loader(){
    var tempdata;
    var time = 0;
    const url_string = window.location.href;
    const vlannumber = new URL(decodeURIComponent(url_string)).searchParams.get("vlannumber");
    const vlanname = new URL(decodeURIComponent(url_string)).searchParams.get("vlanname");
    const vlanip = new URL(decodeURIComponent(url_string)).searchParams.get("vlanip");
    const vlanmask = new URL(decodeURIComponent(url_string)).searchParams.get("vlanmask");

    
}