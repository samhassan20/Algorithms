package com.example.manoj.sortinghat;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.VideoView;

public class string_large extends AppCompatActivity {

    VideoView stringLargeVideo;
    Uri uri;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_string_large);

        stringLargeVideo = findViewById(R.id.videoView_sl);
        Button nl_button = findViewById(R.id.button_sl);
        uri = Uri.parse("android.resource://"+getPackageName()+"/"+R.raw.qs);
        stringLargeVideo.setVideoURI(uri);
        nl_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(stringLargeVideo.isPlaying()){
                    stringLargeVideo.pause();
                } else {
                    stringLargeVideo.start();
                }
            }
        });

    }
}