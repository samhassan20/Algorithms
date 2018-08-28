package com.example.manoj.sortinghat;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.VideoView;

public class string_small extends AppCompatActivity {

    VideoView stringSmallVideo;
    Uri uri;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_string_small);

        stringSmallVideo = findViewById(R.id.videoView_ss);
        Button nl_button = findViewById(R.id.button_ss);
        uri = Uri.parse("android.resource://"+getPackageName()+"/"+R.raw.is);
        stringSmallVideo.setVideoURI(uri);
        nl_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (stringSmallVideo.isPlaying()) {
                    stringSmallVideo.pause();
                } else {
                    stringSmallVideo.start();
                }
            }
        });

    }
}