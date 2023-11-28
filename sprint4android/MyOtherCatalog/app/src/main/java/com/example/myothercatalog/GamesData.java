package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.Serializable;

public class GamesData implements Serializable {
    private String name;
    private String imageUrl;
    private String description;
    public GamesData(JSONObject json){
        try {
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
            this.description= json.getString("description");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }

    public String getName(){
        return name;
    }

    public String getImageUrl() {
        return imageUrl;
    }

    public String getDescription(){return description;}
}
