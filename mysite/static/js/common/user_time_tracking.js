var loadBtn = document.getElementById("load-priority");
var articleContainer = document.getElementById("articleContainer");

// loadBtn.addEventListener("click", function(){
//     axios.get("http://localhost:8000/profile/time_tracking_report_js").then(function (response){
//        articleContainer.innerHTML = response.data;
//     }).catch(function(err){
//         console.log(err);
//     })
// });

var form = document.getElementById("time-tracking-form")
form.addEventListener("click", function(e){
    e.preventDefault()
    var fd = new FormData()
    fd.append("")
})
