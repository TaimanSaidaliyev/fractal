var today = new Date();
var minutes = today.getMinutes()
var hour = today.getHours()

if (minutes < 10){
    minutes = "0" + minutes
}

if (hour < 10){
    hour = "0" + hour
}

date = hour + ':' + minutes

document.getElementById('date-time').innerHTML=date;


$("#kt_datepicker_bdate").flatpickr({
    dateFormat: "d.m.Y",
});

$("#kt_datepicker_edate").flatpickr({
    dateFormat: "d.m.Y",
});

$("#kt_datepicker_tdate").flatpickr({
    dateFormat: "d.m.Y",
});

