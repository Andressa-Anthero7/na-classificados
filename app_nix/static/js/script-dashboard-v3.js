$(document).ready(function(){
    //Comportamento da sidebar no device máximo de 768px
    var withdWindow = $(window).width();
    if(withdWindow  <= 766){
        $('.sidebar').css({'margin-top':'1.2em'})
        $('.sidebar a').css({'max-width':'12%','position':'relative','left':'-0.5em'});
        $('.sidebar p').css({'display':'none'});
        
        $('.sidebar').hover(
            function(){
                $('.txt-btn-sidebar-mobile').css({'position':'relative','left':'-1em'});
                $('.txt-btn-sidebar-mobile-expandir').css({'position':'relative','left':'-0.5em'});
                $('.txt-btn-sidebar-mobile-leads').css({'position':'relative','left':'-0.3em'});
                $('.txt-btn-sidebar-mobile-config').css({'position':'relative','left':'-0.5em'}).text("Config");
                $('.sidebar p').css({'display':'inline','font-size':'12px','position':'relative','top':'-1.2em'});
                $('.sidebar a').css({'max-width':'12%','margin-left':'0'});
                $(".meu-paragrafo");
            },
            function(){
                $('.sidebar').css({'margin-top':'1.2em'})
                $('.sidebar a').css({'max-width':'12%','position':'relative','left':'-0.5em'});
                $('.sidebar p').css({'display':'none'});
            }
            
        );
    }else{

        // Quando o mouse entrar e sair do link (hover)
        $('#chevron-sidebar').hover(
            function() {
                // Quando o mouse entra (hover)
                $(this).css({'background-color': '#495057'});
                $('.content').css({'margin-left':'200px'});
                $('.sidebar p').css({'display':'inline','font-size':'16px','margin-left':'0.5em'});
                $('.sidebar').css({'width':'180px'});
            },
            function() {
                // Quando o mouse sai (reverter as mudanças)
                $(this).css({'background-color': ''}); // Remove o fundo aplicado
                $('.content').css({'margin-left':'45px','padding':'20px','margin-top':'56px'}); // Reverte o margin-left
                $('.sidebar p').css({'display':'none'}); // Oculta os parágrafos
                $('.sidebar').css({'width':'45px'}); // Volta para a largura original
            }
        );
    }


    
});
