!function () 
{ 
    "use strict"; 
    window.addEventListener("load", function () 
    { 
        var e = document.getElementsByClassName("needs-validation"); 
        Array.prototype.filter.call(e, function (t) 
        { 
            $('button[type=submit]').on('click', function() {
                t.addEventListener("submit", function (e) 
                { 
                    !1 === t.checkValidity() && (e.preventDefault(), e.stopPropagation()), t.classList.add("was-validated")
                    if ($(".invalid-feedback:visible").length == 0 && !$('#modal').hasClass('show')) {
                        $('#modal').modal('show') && (e.preventDefault(), e.stopPropagation());
                    }
                    else if ($(".invalid-feedback:visible").length == 0 && $(".valid-feedback:visible").length > 0 && $('#modal').hasClass('show')) {
                        e.preventDefault(), e.stopPropagation()
                        // $("#submit-form").on('click', function() {
                            if ($(".invalid-feedback:visible").length == 0 && $(".valid-feedback:visible").length > 0) {
                                $.ajax ({
                                    method: "POST",
                                    url: `/verify-admin/`,

                                    data: {
                                        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                                        user: document.getElementById('v-username').value,
                                        pass: document.getElementById('v-password').value,
                                    },
                                    success: function(response) {
                                        // r = response.data;
                                        // console.log(r);
                                        if (response.data.valid == "YES") {
                                            console.log('yes')
                                            $("#form1").trigger('submit', [true]);
                                        }
                                        else {
                                            console.log('no')
                                            e.preventDefault(), e.stopPropagation()
                                            $('#alert_placeholder').html('<div class="alert alert-danger alert-dismissible fade show" role="alert">Invalid Admin Credentials!<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>')
                                        }
                                    }
                                })
                            }
                        // })
                    }
                    else {
                        e.preventDefault(), e.stopPropagation()
                    }
                }, !1) 
            })
        })
    }, !1) 
}(), 
window.onload=function(){
    var e=document.getElementById("pristine-valid-example"), t=new Pristine(e);
    e.addEventListener("submit",function(e){
        e.preventDefault();
        t.validate()
    });
    var n=document.getElementById("pristine-valid-common"), i=new Pristine(n);
    n.addEventListener("submit",function(e){
        e.preventDefault();
        i.validate()
    });
    var e=document.getElementById("pristine-valid-specificfield"), a=new Pristine(e), n=document.getElementById("specificfield");
    a.addValidator(n,function(e,t){
        return!(!e.length||e[0]!==e[0].toUpperCase())
    },"The first character must be capitalized",2,!1),
    e.addEventListener("submit",function(e){e.preventDefault();a.validate()})
};