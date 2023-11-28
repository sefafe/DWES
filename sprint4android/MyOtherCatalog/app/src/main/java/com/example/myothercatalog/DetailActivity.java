package com.example.myothercatalog;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import com.bumptech.glide.Glide;

public class DetailActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Recupera los datos pasados en el Intent
        GamesData data = (GamesData) getIntent().getSerializableExtra("data");

        // Encuentra las vistas en las que mostrar los datos
        TextView nameView = findViewById(R.id.game_name_text_view);
        ImageView imageView = findViewById(R.id.game_image_view);
        TextView descView = findViewById(R.id.game_description_text_view);

        // Configura las vistas para mostrar los datos
        nameView.setText(data.getName());
        Glide.with(this).load(data.getImageUrl()).into(imageView);
        descView.setText(data.getDescription());
    }
}
