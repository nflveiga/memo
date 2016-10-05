$( document ).ready(function() {

    
    $( '#calculate' ).click(function() {
        var chooseRythm=$('input[name=rythmConvert]:checked').val()
        var weight=$( '#weight' ).val();
        var concentration=$( '#concentration' ).val();
        var rythm=$( '#rythm' ).val();
        if(chooseRythm && weight && concentration && rythm){
            if(chooseRythm=='to_mcg_kg_min'){
                var result=((concentration*1000)*rythm)/weight/60
                result=Number(Math.round(result+'e2')+'e-2');
                $( '#result' ).html(result + ' mcg/kg/min')
            }
            else if(chooseRythm=='to_ml_h'){
                var result=(rythm*60*weight)/1000/concentration
                result=Number(Math.round(result+'e2')+'e-2');
                $( '#result' ).html(result + ' ml/h')
            }
  
        }
    })
})