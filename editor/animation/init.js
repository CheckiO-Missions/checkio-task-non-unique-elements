//Dont change it
//Dont change it
requirejs(['ext_editor_io', 'jquery_190'],
    function (extIO, $) {
        
        var $tryit;

        var io = new extIO({
            functions: {
                js: 'nonUniqueElements',
                python: 'checkio'
            },
            tryit:function (this_e) {
                $tryit = this_e.extSetHtmlTryIt(this_e.getTemplate('tryit')).find(".tryit-content");
            


                $tryit.find('.bn-check').click(function(e){
                    var $input = $tryit.find('.input-list');
                    var inputList = $input.val().split(" ");
                    var tryList = [];
                    for (var i = 0; i < inputList.length; i++) {
                        if (isNaN(inputList[i]) || inputList[i] === "") {
                            continue;
                        }
                        tryList.push(Number(inputList[i]));
                    }
                    $input.val(tryList.join(" "));
                    this_e.extSendToConsoleCheckiO(tryList);
                    e.stopPropagation();
                    return false;
                });

            },
            retConsole: function (ret) {
                try {
                    ret = JSON.parse(ret);
                } catch (err) {}
                $tryit.find('.checkio-result').html("Checkio return<br>" + JSON.stringify(ret));
            }
        });
        io.start();
    }
);
