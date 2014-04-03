$(document).ready(function(e){

	//// 縦ラインを可視化  ////
	function setVirtical(day_num){
		var day_class = '.day_' + day_num;

		$(day_class).hover(function(){
			$(day_class).addClass('active');
		},function(){
			$(day_class).removeClass('active');		  
		});
	}

	var d_count = $('tbody>tr:first>td').length;	//テーブルの一列目tdの総数

	//// ドロップダウン ////
	function setOpen(staff_id,day_num){	//staff_idと順番は無関係だと思われるので注意,name?
		var dropdown_id = '#s' + staff_id + 'd' + day_num;
		var dropdown_menu_id = dropdown_id + '_mn';

		var timer;
		$(dropdown_id).hover(function(){
			timer = setTimeout(function(){
				$(dropdown_menu_id).show();
			},500);		  
		},function(){
			clearTimeout(timer);
			$(dropdown_menu_id).hide();		  
		});

	}


	var s_count = $('tbody>tr>th').length;

	/* 定義した内容をセット */
	for(var i=1;i<=d_count;i++){
		var d_num = i.toString();
		setVirtical(d_num);

		for(var j=1;j<=s_count;j++){
			var s_num = j.toString();
			setOpen(s_num,d_num);		  
		}
	}

/*	$('a#postes').click(function(e){
		console.log("try");
		$.post('',{'staff':'1','day':'10'},'JSON');	  
		//return false;
	});*/

/*	$.post('',{'name':"me"},function(){
		alert("ok");		  
	},'JSON');*///権限がない？

	var checked_all = $('input:checked');

	/*checked_all.each(function(){
		var parent_id = this.name.split('_dt')[0];		  
		$('#' + parent_id).append('<strong>' + this.value + '</strong>');
	});*/

	$('.rd').click(function(){
		var mystaff = $(this).attr('staff_id');
		var mydate = $(this).attr('date');
		var form = $('form.t_form:has(input[type="hidden"][name="staff"][value="'+mystaff+'"])').filter(':has(input[type="hidden"][name="date"][value="'+mydate+'"])');
		form.submit();
	});
});
