$( '#raptr-nav .navbar-nav a' ).on( 'click', function () {
	  $( '#raptr-nav .navbar-nav' ).find( 'li.active' ).removeClass( 'active' );
	  $( this ).parent( 'li' ).addClass( 'active' );
});