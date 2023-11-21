package com.example.myothercatalog;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class GamesRecyclerViewAdapter extends RecyclerView.Adapter<GamesViewHolder> {
    private List<GamesData> allData;
    private Activity activity;

    public GamesRecyclerViewAdapter(List<GamesData> dataSet, Activity activity){
        this.allData=dataSet;
        this.activity=activity;
    }

    public GamesViewHolder onCreateViewHolder(@NonNull ViewGroup parent,int viewType){
        View view= LayoutInflater.from(parent.getContext()).inflate(R.layout.games_view_holder,parent,false);
        return new GamesViewHolder(view);
    }

    public void onBindViewHolder (GamesViewHolder holder, int position){
        GamesData dataInPositionToBeRendered= allData.get(position);
        holder.showData(dataInPositionToBeRendered,activity);
    }

    public int getItemCount(){
        return allData.size();
    }
}
