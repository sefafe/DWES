package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class GamesViewHolder extends RecyclerView.ViewHolder {
private final TextView textView;
private final ImageView imageView;

public GamesViewHolder(@NonNull View itemView){
    super (itemView);
    textView= itemView.findViewById(R.id.game_name_text_view);
    imageView= itemView.findViewById(R.id.game_image_view);
}

public void showData(GamesData data, Activity activity){
    textView.setText(data.getName());
    Glide.with(itemView.getContext()).load(data.getImageUrl()).into(imageView);
}
}
