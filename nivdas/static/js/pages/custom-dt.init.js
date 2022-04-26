
$(document).ready(function () {
    $("#datatable").DataTable(),
    $('#datatable-buttons thead tr')

    // var x = $('#datatable-buttons thead th').length;

    var table = $('#datatable-buttons').DataTable({
        orderCellsTop: true,
        fixedHeader: true,
        lengthChange: !1,
        buttons: ["copy", "excel", "pdf", "colvis"],
        initComplete: function () {

            // for (let i=0; i<x; i++){
            //     this.api().columns(i).every(function () {
            //         var column = this;
            //         var select = $('<select class="form-select"><option value="">All</option></select>')
            //             // .appendTo(myTable.header())
            //             .appendTo("#datatable-buttons thead tr #sort")
            //             .on('change', function () {
            //                 var val = $.fn.dataTable.util.escapeRegex(
            //                     $(this).val()
            //                 );

            //                 column
            //                     .search(val ? '^' + val + '$' : '', true, false)
            //                     .draw();
            //             });

            //         column.data().unique().sort().each(function (d, j) {
            //             select.append('<option value="' + d + '">' + d + '</option>')
            //         });
            //     })
            // }



            this.api().columns(0).every(function () {
                var column = this;
                var select = $(' <select class="form-select"><option value=""></option></select>')
                    // .appendTo(myTable.header())
                    .appendTo('#datatable-buttons thead tr #sort0')
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            })

            this.api().columns(1).every(function () {
                var column = this;
                var select = $(' <select class="form-select"><option value=""></option></select>')
                    // .appendTo(myTable.header())
                    .appendTo('#datatable-buttons thead tr #sort1')
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            })

            this.api().columns(2).every(function () {
                var column = this;
                var select = $(' <select class="form-select"><option value=""></option></select>')
                    // .appendTo(myTable.header())
                    .appendTo('#datatable-buttons thead tr #sort2')
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            })

            this.api().columns(3).every(function () {
                var column = this;
                var select = $(' <select class="form-select"><option value=""></option></select>')
                    // .appendTo(myTable.header())
                    .appendTo('#datatable-buttons thead tr #sort3')
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            })

            this.api().columns(4).every(function () {
                var column = this;
                var select = $(' <select class="form-select"><option value=""></option></select>')
                    // .appendTo(myTable.header())
                    .appendTo('#datatable-buttons thead tr #sort4')
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            })

            this.api().columns(5).every(function () {
                var column = this;
                var select = $(' <select class="form-select"><option value=""></option></select>')
                    // .appendTo(myTable.header())
                    .appendTo('#datatable-buttons thead tr #sort5')
                    .on('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search(val ? '^' + val + '$' : '', true, false)
                            .draw();
                    });

                column.data().unique().sort().each(function (d, j) {
                    select.append('<option value="' + d + '">' + d + '</option>')
                });
            })

        },
    }).buttons().container().appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)");
    $(".dataTables_length select").addClass("form-select form-select-sm")
});