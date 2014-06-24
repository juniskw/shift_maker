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

	$('.toggle_switch').hover(function(){
		$('.dropdown-menu:visible').hide();
	});

	$('.toggle_switch').click(function(){
		//$('.dropdown-menu:visible').hide();
		var dropdown_menu = $(this.children[0].children[1]);
		dropdown_menu.show();
	});

	$('.worktime_choices').click(function(){
		$.ajax({
			'url':'edit/',
			'type':'POST',
			'data':{
				'staff_id':$(this).attr('staff_id'),
				'worktime_id':$(this).attr('worktime_id'),
				'year':$(this).attr('year'),
				'month':$(this).attr('month'),
				'day':$(this).attr('day'),
			},
			'dataType':'text',
			'success':function(resp){
				$('div:has(.dropdown-menu:visible) > a > strong').text(resp);
			},
		});		  
	});

	var s_count = $('tbody>tr>th').length;

	/* 定義した内容をセット */
	for(var i=1;i<=d_count;i++){
		var d_num = i.toString();
		setVirtical(d_num);
	}
});
