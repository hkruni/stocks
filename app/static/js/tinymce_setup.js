tinymce.init({
    //选择class为content的标签作为编辑器
    selector: '#content',
    //方向从左到右
    directionality:'ltr',
    //语言选择中文
    language:'zh_CN',
    //高度为400
    height:1200,
    //工具栏上面的补丁按钮
    plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'save table contextmenu directionality emoticons template paste textcolor',
            'codesample',
    ],
    //工具栏的补丁按钮
     toolbar: 'insertfile undo redo | \
     styleselect | \
     bold italic | \
     alignleft aligncenter alignright alignjustify | \
     bullist numlist outdent indent | \
     link image | \
     print preview media fullpage | \
     forecolor backcolor emoticons |\
     codesample fontsizeselect fullscreen|\
     table tabledelete | tableprops tablerowprops tablecellprops | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol',
    //字体大小
    fontsize_formats: '10pt 12pt 14pt 18pt 24pt 36pt',
    //按tab不换行
    nonbreaking_force_tab: true,
    //images_upload_url: '/stocks/uploadimage',
    paste_data_images: true,
    images_upload_handler: (blobInfo, success, failure) => {
           let base64 = "data:image/png;base64," + blobInfo.base64();
           success(base64);
    }
});