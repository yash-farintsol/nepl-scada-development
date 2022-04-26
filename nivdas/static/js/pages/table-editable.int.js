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
            console.log(this.getAttribute('data-id'))
            localStorage.setItem('id', this.getAttribute('data-id'))
            var ID1 = localStorage.id;
            console.log(ID1)
            $(`#down${ID1}`).value = $(`#drop${ID1}`).value
            console.log($(`#down${ID1}`).value)

        },
        save:function(t){
            console.log(this.getAttribute('data-id'))
            localStorage.setItem('id', this.getAttribute('data-id'))
            var ID1 = localStorage.id;
            console.log(ID1)
            $(`#down${ID1}`).value = $(`#drop${ID1}`).value
            console.log($(`#down${ID1}`).value)
            $('#modal').modal('show');

            $(".edit i",this).removeClass("fa-save").addClass("fa-pencil-alt").attr("title","Edit"),
            this in e&&(e[this].destroy(),delete e[this])
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