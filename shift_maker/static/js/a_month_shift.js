$(document).ready(function(e){

	//// 縦ラインを可視化  ////

	function getDayShift(stf_shft,indx_nm){
		var day_shifts = [];

		$.each(stf_shft,function(){
			var day_shift = $(this).children()[indx_nm];
			day_shifts.push(day_shift);
		});
		return day_shifts;
	}

	var shifts = $('tr');

	$('.table_in').hover(function(){
		var index_num = $(this).index();

		$.each(getDayShift(shifts,index_num),function(){
			$(this).addClass('active'); 
		});
	},function(){
		var index_num = $(this).index();
		
		$.each(getDayShift(shifts,index_num),function(){
			$(this).removeClass('active');		  
		})		  
	});

	
	//// ドロップダウン ////

	$('.toggle_switch').hover(function(){
		$('.dropdown-menu:visible').hide();
	});

	$('.toggle_switch').click(function(){
		var dropdown_menu = $(this.children[0].children[1]);
		dropdown_menu.show();
	});

	$('.worktime_choices').click(function(){
		var staff_id = $(this).attr('staff_id');
		var worktime_id = $(this).attr('worktime_id');
		$.ajax({
			'url':'edit/',
			'type':'POST',
			'data':{
				'staff_id':staff_id,
				'worktime_id':worktime_id,
				'year':$(this).attr('year'),
				'month':$(this).attr('month'),
				'day':$(this).attr('day'),
			},
			'dataType':'text',
			'success':function(resp){
				$('div:has(.dropdown-menu:visible) > a > strong').text(resp);
				var total_count = $('.table_in[staff_id="' + staff_id + '"]' + '[worktime_id=' + worktime_id + ']');
				total_count.text( parseInt(total_count.text()) + 1 );
			},
		});		  
	});

});
