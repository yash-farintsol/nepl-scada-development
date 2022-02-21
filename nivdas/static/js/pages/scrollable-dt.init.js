$(document).ready(function(){
    $("#datatable").DataTable()
    $('#datatable-buttons thead tr')

    var table = $('#datatable-buttons').DataTable({
        // scrollX: true,
        orderCellsTop: true,
        fixedHeader: true,
        lengthChange:!1,
        buttons:["copy","excel","colvis"],
        initComplete: function () {

            this.api().columns(0).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort0')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(1).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#username')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(2).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort2')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(3).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort3')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(4).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort4')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(5).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort5')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(6).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort6')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(7).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort7')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(8).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort8')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })
            this.api().columns(9).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort9')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                select.append( '<option value="Male">Male</option>' )
                select.append( '<option value="Female">Female</option>' )
            })
            this.api().columns(10).every( function ()
            {
                var column = this;
                var select = $(' <select class="form-select"><option value="">All</option></select>')
                    .appendTo('#datatable-buttons thead tr #sort10')
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                });
            })

        },

    }).columns.adjust().buttons().container().appendTo("#datatable-buttons_wrapper .col-md-6:eq(0)");
    $(".dataTables_length select").addClass("form-select form-select-sm")
});