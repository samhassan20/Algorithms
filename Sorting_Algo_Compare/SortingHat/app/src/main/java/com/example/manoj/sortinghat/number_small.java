package com.example.manoj.sortinghat;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.VideoView;

public class number_small extends AppCompatActivity {

    VideoView numbersmallVideo;
    Uri uri;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_number_small);

        numbersmallVideo = findViewById(R.id.videoView_ns);
        Button nl_button = findViewById(R.id.button_ns);
        uri = Uri.parse("android.resource://"+getPackageName()+"/"+R.raw.cs);
        numbersmallVideo.setVideoURI(uri);
        nl_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
            if(numbersmallVideo.isPlaying()){
                numbersmallVideo.pause();
            } else {
                numbersmallVideo.start();
            }
        }
        });

    }
}