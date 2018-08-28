package com.example.manoj.sortinghat;

import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.VideoView;

public class number_large extends AppCompatActivity {

    VideoView numberLargevideo;
    Uri uri;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_number_large);

        numberLargevideo = findViewById(R.id.videoView_nl);
        Button nl_button = findViewById(R.id.button_nl);
        uri = Uri.parse("android.resource://"+getPackageName()+"/"+R.raw.hs);
        numberLargevideo.setVideoURI(uri);
        nl_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(numberLargevideo.isPlaying()){
                    numberLargevideo.pause();
                } else {
                    numberLargevideo.start();
                }
            }
        });
    }
}
