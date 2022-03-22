// $(function(){
//     var e={};
//     $(".table-edits tr").editable({
//         dropdowns:{gender:["Male","Female"]},
//         edit:function(t){
//             $(".edit i",this).removeClass("fa-pencil-alt").addClass("fa-save").attr("title","Save")
//         },
//         save:function(t){
//             $(".edit i",this).removeClass("fa-save").addClass("fa-pencil-alt").attr("title","Edit"),this in e&&(e[this].destroy(),delete e[this])
//         },cancel:function(t){
//             $(".edit i",this).removeClass("fa-save").addClass("fa-pencil-alt").attr("title","Edit"),this in e&&(e[this].destroy(),delete e[this])
//         }
//     })
// });






$(function(){
    var e={};
    $(".table-edits tr").editable({
        dropdowns:{eqp_status:["Active","InActive"]},
        edit:function(t){
            $(".edit i",this).removeClass("fa-pencil-alt").addClass("fa-save").attr("title","Save")
        },
        save:function(t){
            $('#modal').modal('show');
            $(".edit i",this).removeClass("fa-save").addClass("fa-pencil-alt").attr("title","Edit"),
            this in e&&(e[this].destroy(),delete e[this])
            // var forms = document.querySelectorAll('.needs-validation')
            // Array.prototype.slice.call(forms).forEach(function (t) {
            //     t.addEventListener('submit', function (e) {
            //         if (!t.checkValidity()) {
            //             e.preventDefault()
            //             e.stopPropagation()
            //         }
            //         else {

            //         }

            //         t.classList.add('was-validated')
            //     }, false)
            // })
        },
        cancel:function(t){
            $(".edit i",this).removeClass("fa-save").addClass("fa-pencil-alt").attr("title","Edit"),
            this in e&&(e[this].destroy(),delete e[this])
        }
    })
});


// $(function(){
//     var e={};
//     $(".table-edits tr").editable({
//         dropdowns:{eqp_status:["Active","InActive"]},
//         edit:function(t){
//             $(".edit i",this).removeClass("fa-pencil-alt").addClass("fa-save").attr("title","Save")
//         },
//         save:function(t){
//             $('#modal').modal('show');
//             $(".edit i",this).removeClass("fa-save").addClass("fa-pencil-alt").attr("title","Edit"),
//             this in e&&(e[this].destroy(),delete e[this])
//         },
//         cancel:function(t){
//             $(".edit i",this).removeClass("fa-save").addClass("fa-pencil-alt").attr("title","Edit"),
//             this in e&&(e[this].destroy(),delete e[this])
//         }
//     })
// });