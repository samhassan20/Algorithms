package com.example.manoj.sortinghat;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Spinner dataTypeSpinner = findViewById(R.id.data_type_spinner);
        final Spinner dataSizeSpinner = findViewById(R.id.data_size_spinner);
        final Button goButton = findViewById(R.id.Go_Button);

        ArrayAdapter<String> dtAdapter = new ArrayAdapter<String>(MainActivity.this,
                android.R.layout.simple_list_item_1, getResources().getStringArray(R.array.data_type));
        dtAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        dataTypeSpinner.setAdapter(dtAdapter);

        ArrayAdapter<String> dsAdapter = new ArrayAdapter<String>(MainActivity.this,
                android.R.layout.simple_list_item_1, getResources().getStringArray(R.array.data_size));
        dsAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        dataSizeSpinner.setAdapter(dsAdapter);

        goButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                final Intent myintent;
                if((dataTypeSpinner.getSelectedItem().toString().trim().equals("---Select---")) ||
                        (dataSizeSpinner.getSelectedItem().toString().trim().equals("---Select---"))){
                    Toast.makeText(view.getContext(), "Please select from the options", Toast.LENGTH_LONG).show();
                }
                else if((dataTypeSpinner.getSelectedItem().toString().trim().equals("Number")) &&
                        (dataSizeSpinner.getSelectedItem().toString().trim().equals("Small"))){
                    Toast.makeText(view.getContext(), "Case 1", Toast.LENGTH_LONG).show();
                    myintent = new Intent(MainActivity.this,number_small.class);
                    startActivityForResult(myintent,1);
                }

                else if((dataTypeSpinner.getSelectedItem().toString().trim().equals("Number")) &&
                        (dataSizeSpinner.getSelectedItem().toString().trim().equals("Medium"))){
                    Toast.makeText(view.getContext(), "Case 2", Toast.LENGTH_LONG).show();
                    myintent = new Intent(MainActivity.this,number_medium.class);
                    startActivityForResult(myintent,1);
                }

                else if((dataTypeSpinner.getSelectedItem().toString().trim().equals("Number")) &&
                        (dataSizeSpinner.getSelectedItem().toString().trim().equals("Large"))){
                    Toast.makeText(view.getContext(), "Case 3", Toast.LENGTH_LONG).show();
                    myintent = new Intent(MainActivity.this,number_large.class);
                    startActivityForResult(myintent,1);
                }
                else if((dataTypeSpinner.getSelectedItem().toString().trim().equals("String")) &&
                        (dataSizeSpinner.getSelectedItem().toString().trim().equals("Small"))){
                    Toast.makeText(view.getContext(), "Case 4", Toast.LENGTH_LONG).show();
                    myintent = new Intent(MainActivity.this,string_small.class);
                    startActivityForResult(myintent,1);
                }

                else if((dataTypeSpinner.getSelectedItem().toString().trim().equals("String")) &&
                        (dataSizeSpinner.getSelectedItem().toString().trim().equals("Medium"))){
                    Toast.makeText(view.getContext(), "Case 5", Toast.LENGTH_LONG).show();
                    myintent = new Intent(MainActivity.this,string_medium.class);
                    startActivityForResult(myintent,1);
                }

                else{
                    Toast.makeText(view.getContext(), "Case 6", Toast.LENGTH_LONG).show();
                    myintent = new Intent(MainActivity.this,string_large.class);
                    startActivityForResult(myintent,1);

                }
            }
        });

    }
}
