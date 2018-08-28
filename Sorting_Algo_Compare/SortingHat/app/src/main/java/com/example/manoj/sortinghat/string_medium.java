package com.example.manoj.sortinghat;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.VideoView;

public class string_medium extends AppCompatActivity {

    VideoView stringMediumVideo;
    Uri uri;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_string_medium);

        stringMediumVideo = findViewById(R.id.videoView_sm);
        Button nl_button = findViewById(R.id.button_sm);
        uri = Uri.parse("android.resource://"+getPackageName()+"/"+R.raw.ms);
        stringMediumVideo.setVideoURI(uri);
        nl_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (stringMediumVideo.isPlaying()) {
                    stringMediumVideo.pause();
                } else {
                    stringMediumVideo.start();
                }
            }
        });

    }
}