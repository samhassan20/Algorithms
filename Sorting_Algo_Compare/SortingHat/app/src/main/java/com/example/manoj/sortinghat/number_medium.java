package com.example.manoj.sortinghat;

import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.VideoView;

public class number_medium extends AppCompatActivity {

    VideoView numberMediumvideo;
    Uri uri;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_number_medium);

        numberMediumvideo = findViewById(R.id.videoView_nm);
        Button nl_button = findViewById(R.id.button_nm);
        uri = Uri.parse("android.resource://"+getPackageName()+"/"+R.raw.ms);
        numberMediumvideo.setVideoURI(uri);
        nl_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(numberMediumvideo.isPlaying()){
                    numberMediumvideo.pause();
                } else {
                    numberMediumvideo.start();
                }
            }
        });

    }
}